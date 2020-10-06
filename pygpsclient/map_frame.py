'''
Mapview frame class for PyGPSClient application.

This handles a frame containing a location map downloaded via a MapQuest API.

*****************************************************************************
NOTE: The free MapQuest API key is subject to a limit of 15,000 
transactions / month, or roughly 500 / day, so the map updates are only
run periodically (once a minute). This utility is NOT intended to be used for
real time navigation.
*****************************************************************************

Created on 13 Sep 2020

@author: semuadmin
'''

from io import BytesIO
from time import time
from tkinter import Frame, Canvas, font, NW, N, S, E, W

from PIL import ImageTk, Image
import requests

from .globals import WIDGETU2, MAPURL, MAP_UPDATE_INTERVAL, \
                                IMG_WORLD, ICON_POS
from .strings import NOWEBMAPERROR1, NOWEBMAPERROR2, NOWEBMAPERROR3, \
                                NOWEBMAPERROR4, NOWEBMAPERROR5


class MapviewFrame(Frame):
    '''
    Frame inheritance class for plotting satellite view.
    '''

    def __init__(self, app, *args, **kwargs):
        '''
        Constructor.
        '''

        self.__app = app  # Reference to main application class
        self.__master = self.__app.get_master()  # Reference to root class (Tk)

        Frame.__init__(self, self.__master, *args, **kwargs)

        def_w, def_h = WIDGETU2
        self.width = kwargs.get('width', def_w)
        self.height = kwargs.get('height', def_h)
        self._img = None
        self._marker = None
        self._last_map_update = 0
        self._body()

        self.bind("<Configure>", self._on_resize)

    def _body(self):
        '''
        Set up frame and widgets.
        '''

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.can_mapview = Canvas(self, width=self.width, height=self.height, bg="white")
        self.can_mapview.grid(column=0, row=0, sticky=(N, S, E, W))

    def update_map(self, lat, lon, hacc, vacc, fix, static=True):
        '''
        Draw map and mark current known position.
        '''

        w, h = self.width, self.height
        resize_font = font.Font(size=min(int(w / 20), 14))

        if fix == 'NO FIX':
            self.can_mapview.delete("all")
            self.reset_map_refresh()
            self.can_mapview.create_text(w / 2, h / 2 - (w / 20), text=NOWEBMAPERROR1,
                                         fill="red", font=resize_font)
            self.can_mapview.create_text(w / 2, h / 2 + (w / 20), text=NOWEBMAPERROR5,
                                         fill="red", font=resize_font)
            return

        if static:
            self._draw_static_map(lat, lon)
        else:
            self._draw_web_map(lat, lon, hacc, vacc)

    def _draw_static_map(self, lat, lon):
        '''
        Draw fixed scale Mercator world map
        '''

        OFFSET_X = 0
        OFFSET_Y = 0

        w, h = self.width, self.height
        self.can_mapview.delete("all")
        self._img = ImageTk.PhotoImage(Image.open(IMG_WORLD).resize((w, h), Image.ANTIALIAS))
        self._marker = ImageTk.PhotoImage(Image.open(ICON_POS))
        self.can_mapview.create_image(0, 0, image=self._img, anchor=NW)
        x = (w / 2) + (lon * (w / 360)) + OFFSET_X
        y = (h / 2) - (lat * (h / 180)) + OFFSET_Y
        self.can_mapview.create_image(x, y, image=self._marker, anchor=S)

    def _draw_web_map(self, lat, lon, hacc, vacc):
        '''
        Draw scalable web map via MapQuest API
        '''

        w, h = self.width, self.height
        resize_font = font.Font(size=min(int(w / 20), 14))

        apikey = self.__app.api_key
        if apikey == '':
            self.can_mapview.delete("all")
            self.reset_map_refresh()
            self.can_mapview.create_text(w / 2, h / 2 - (w / 20), text=NOWEBMAPERROR1,
                                         fill="orange", font=resize_font)
            self.can_mapview.create_text(w / 2, h / 2 + (w / 20), text=NOWEBMAPERROR2,
                                         fill="orange", font=resize_font)
            return

        now = time()
        if now - self._last_map_update < MAP_UPDATE_INTERVAL:
            self._draw_countdown((-360 / MAP_UPDATE_INTERVAL) * (now - self._last_map_update))
            return
        else:
            self._last_map_update = now

        url = self._format_url(apikey, lat, lon, hacc, vacc)

        try:
            response = requests.get(url)
            if response.status_code == 200:
                img_data = response.content
                self._img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
                self.can_mapview.delete("all")
                self.can_mapview.create_image(0, 0, image=self._img, anchor=NW)
                self.can_mapview.update()
        except Exception:  # Complex exception chain with these calls so catch everything
            self.can_mapview.delete("all")
            self.can_mapview.create_text(w / 2, h / 2 - (w / 20), text=NOWEBMAPERROR3,
                                         fill="red", font=resize_font)
            self.can_mapview.create_text(w / 2, h / 2 + (w / 20), text=NOWEBMAPERROR4,
                                         fill="red", font=resize_font)

    def _draw_countdown(self, wait):
        '''
        Draw clock icon indicating time until next scheduled map refresh.
        '''

        self.can_mapview.create_oval((5, 5, 20, 20), fill="#616161", outline="")
        self.can_mapview.create_arc((5, 5, 20, 20), start=90, extent=wait, \
                                            fill="#ffffff", outline="")
        self.can_mapview.update()

    def _format_url(self, apikey, lat, lon, hacc, vacc):
        '''
        Formats URL for web map download.
        '''

        w, h = self.width, self.height
        zoom = self.__app.frm_settings.get_settings()['mapzoom']
        radius = str(hacc / 1000) # km

        return MAPURL.format(apikey, lat, lon, zoom, radius, lat, lon, w, h)

    def reset_map_refresh(self):
        '''
        Reset map refresh counter to zero
        '''

        self._last_map_update = 0

    def _on_resize(self, event):
        '''
        Resize frame
        '''

        self.width, self.height = self.get_size()

    def get_size(self):
        '''
        Get current canvas size.
        '''

        self.update_idletasks()  # Make sure we know about any resizing
        width = self.can_mapview.winfo_width()
        height = self.can_mapview.winfo_height()
        return (width, height)

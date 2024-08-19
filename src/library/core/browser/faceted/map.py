# -*- coding: utf-8 -*-
from collective.faceted.map.browser.view import FacetedGeoJSON as BaseFacetedGeoJSON
from collective.faceted.map.browser.map import MapView
from plone.api.portal import get_registry_record
from Products.Five import BrowserView

import json


# FolderView
class FacetedMapView(MapView):
    """Faceted map view"""

    def map_configuration(self):
        """Returns global map configuration from registry"""
        map_layers = get_registry_record("geolocation.map_layers") or []
        config = {
            "fullscreencontrol": get_registry_record("geolocation.fullscreen_control"),
            "locatecontrol": get_registry_record("geolocation.locate_control"),
            "zoomcontrol": get_registry_record("geolocation.zoom_control"),
            "minimap": get_registry_record("geolocation.show_minimap"),
            "addmarker": get_registry_record("geolocation.show_add_marker"),
            "geosearch": get_registry_record("geolocation.show_geosearch"),
            "geosearch_provider": get_registry_record("geolocation.geosearch_provider"),
            "default_map_layer": get_registry_record("geolocation.default_map_layer"),
            "map_layers": [
                {"title": "Titre", "id": layer}
                for layer in map_layers
            ],
            "latitude": get_registry_record("geolocation.default_latitude"),
            "longitude": get_registry_record("geolocation.default_longitude"),
        }
        return json.dumps(config)


class FacetedGeoJSONPopup(BrowserView):
    def popup(self, brain):
        url = brain.getURL()
        title = brain.Title
        description = brain.Description
        orientation = self.context.orientation
        # if brain.has_leadimage:
        #     img_url = get_scale_url(brain, self.request, "image", "liste", orientation)
        #     return f"""<a href="{url}" title="{title}">
        #                  <img src="{img_url}" alt="{title}" />
        #                  <div>
        #                    <span class="popup_title">{title}</span>
        #                    <span class="popup_description">{description}</span>
        #                  </div>
        #                </a>"""
        # else:
        return f"""<a href="{url}" title="{title}">
                        <div>
                        <span class="popup_title">{title}</span>
                        <span class="popup_description">{description}</span>
                        </div>
                    </a>"""

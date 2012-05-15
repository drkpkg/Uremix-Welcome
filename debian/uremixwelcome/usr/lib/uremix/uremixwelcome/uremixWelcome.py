#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from gi.repository import Gtk
import commands
import os
import gettext
from user import home
from gi.repository import WebKit
from configobj import ConfigObj
import string

gettext.install("uremixwelcome", "/usr/share/uremix/locale")

class uremixwelcome():
    def __init__(self):
        self.InitUi()
    
    def InitUi(self):
        Builder = Gtk.Builder()
        Builder.add_from_file("/usr/lib/uremix/uremixwelcome/uremixwelcome.glade")
        win = Builder.get_object("main_window")
        
        win.connect("delete-event", Gtk.main_quit)
        win.connect("key-press-event", self.key_press)
                
        sys.path.append('/usr/lib/uremix/common')
        config = ConfigObj("/etc/uremix/info")
        description = config['DESCRIPTION']
        codename = config['CODENAME']
        edition = config['EDITION']
        release = config['RELEASE']
        description = description.replace("\"", "")
        browser = WebKit.WebView()
        scroll = Builder.get_object("scrolled_welcome")
        scroll.add(browser)
        
        subs = {}
        subs['release'] = release + " (" + codename + ")"
        subs['edition'] = edition
        subs['title'] = _("Bienvenido a Uremix Linux")
        subs['release_title'] = _("Lanzamiento")
        subs['edition_title'] = _("Edición")
        subs['discover_title'] = _("Documentación")
        subs['find_help_title'] = _("Soporte y Communidad")
        subs['contribute_title'] = _("Proyecto")
        subs['comunity_title'] = _("Otros Proyectos en Bolivia")
        subs['hacklab'] = _("HackLab Bolivia")
        subs['softlibre'] = _("Software Libre Bolivia")
        subs['mozilla'] = _("Mozilla Bolivia")
        subs['boliviaos'] = _("Bolivia OS")
        subs['uremix_about'] = _("Acerca de Uremix")
        subs['user_guide'] = _("Guia de Usuario (PDF)")
        subs['forums'] = _("Foros")
        subs['sponsor'] = _("Auspiciantes")
        subs['donation'] = _("Donaciones")
        subs['get_involved'] = _("Como involucrarse")
        subs['ideas'] = _("Nuevas Ideas")
        subs['tutorials'] = _("Tutoriales")
        subs['show'] = _("Mostrar este diálogo al iniciar")
        subs['close'] = _("Cerrar")
        if os.path.exists(home + "/.uremix/uremixwelcome/norun.flag"):      
            subs['checked'] = ("")
        else:
            subs['checked'] = ("CHECKED")

        subs['welcome'] = _("Bienvenido y Gracias por elegir Uremix Linux. Esperamos que disfrutes usandolo como nosotros diseñandolo para tí. Los enlaces a continuación te ayudaran a iniciarte con tu nuevo sistema operativo. Pasa un buen rato y no dudes en escribirnos a la lista de correo.")
        template = open("/usr/lib/uremix/uremixwelcome/templates/welcome.html").read()      
        html = string.Template(template).safe_substitute(subs)
        browser.load_html_string(html, "file:/")    
        browser.connect('title-changed', self.title_changed)
        win.add(scroll)
        win.show_all()
        Gtk.main()
        
    def key_press(self,window,event):
        if event.keyval == 65307:
            Gtk.main_quit()
        
    def title_changed(self, view, frame, title):    
        if title.startswith("nop"):
            return
        if title == "event_sponsor":
            os.system("xdg-open http://openit.com.bo")
        elif title == "event_forums":
            os.system("xdg-open http://comunidad.uremix.org/")
        elif title == "event_tutorials":
            os.system("xdg-open http://wiki.uremix.org/")
        elif title == "event_forums":
            os.system("xdg-open http://comunidad.uremix.org/")
        elif title == "event_about":
            os.system("xdg-open http://www.uremix.org/grupo.php")
        elif title == "event_hacklab":
            os.system("xdg-open http://hacklab.org.bo/")
        elif title == "event_softlibre":
            os.system("xdg-open http://www.softwarelibre.org.bo/")
        elif title == "event_boliviaos":
            os.system("xdg-open http://www.boliviaos.org")
        elif title == "event_mozilla":
            os.system("xdg-open http://www.mozillabolivia.org/")
        elif title == "event_ideas":
            os.system("xdg-open http://comunidad.uremix.org/viewforum.php?f=20&sid=e2f9f051b68e6e3180e39dfeffabbdc1")
        
        if title == "event_close_true":
            if os.path.exists(home + "/.uremix/uremixwelcome/norun.flag"):
                os.system("rm -rf " + home + "/.uremix/uremixwelcome/norun.flag")
            Gtk.main_quit()
        elif title == "event_close_false":
            os.system("mkdir -p " + home + "/.uremix/uremixwelcome")        
            os.system("touch " + home + "/.uremix/uremixwelcome/norun.flag")
            Gtk.main_quit()
        elif title == "checkbox_checked":
            if os.path.exists(home + "/.uremix/uremixwelcome/norun.flag"):
                os.system("rm -rf " + home + "/.uremix/uremixwelcome/norun.flag")
        elif title == "checkbox_unchecked":
            os.system("mkdir -p " + home + "/.uremix/uremixwelcome")        
            os.system("touch " + home + "/.uremix/uremixwelcome/norun.flag")


if __name__ == "__main__":
    uremixwelcome()
    #Gtk.main()


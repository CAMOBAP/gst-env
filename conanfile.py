from conans import ConanFile, tools
from conanos.build import config_scheme
import os

class GstenvConan(ConanFile):
    name = "gst-env"
    version = "0.1"
    description = "Helper program to yield configuration script for gstreamer runtime environment"
    url = "https://github.com/conan-multimedia/gst-env"
    topics = ("gstreamer", "runtime environment")
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
    }
    default_options = { 'shared': True }
    gst_bat = r'''
    @ECHO OFF
    SET CONAN_ROOT=%USERPROFILE%\.conan\data
    SET GST_REGISTRY_1_0=%USERPROFILE%\.cache\registry\plugin\gstreamer
    SET GST_PLUGIN_SYSTEM_PATH_1_0=%GST_PLUGIN_SYSTEM_PATH_1_0%
    SET GST_PLUGIN_SCANNER_1_0=%GSTREAMER%\libexec\gstreamer-1.0\gst-plugin-scanner
    SET GIO_EXTRA_MODULES=%GLIB_NETWORKING%\lib\gio\modules
    SET PKG_CONFIG_PATH=%PKG_CONFIG_PATH%
    SET PATH=%GST_PATH_1_0%;%PATH%
    CMD
    '''

    def configure(self):
        del self.settings.compiler.libcxx

        config_scheme(self)

    def requirements(self):
        self.requires.add("AMF/1.4.9@conanos/stable")
        self.requires.add("FFmpeg/3.3.4.r87868@conanos/stable")
        self.requires.add("OpenGL/master@conanos/stable")
        self.requires.add("SDL/2.0.9@conanos/stable")
        self.requires.add("a52dec/0.7.4@conanos/stable")
        self.requires.add("bzip2/1.0.6@conanos/stable")
        self.requires.add("cairo/1.15.12@conanos/stable")
        self.requires.add("expat/2.2.5@conanos/stable")
        self.requires.add("faad2/2.8.8@conanos/stable")
        self.requires.add("flac/1.3.2@conanos/stable")
        self.requires.add("fontconfig/2.13.0@conanos/stable")
        self.requires.add("freetype/2.9.1@conanos/stable")
        self.requires.add("fribidi/1.0.5@conanos/stable")
        self.requires.add("game-music-emu/0.6.2@conanos/stable")
        self.requires.add("gdk-pixbuf/2.38.0@conanos/stable")
        self.requires.add("glib/2.58.1@conanos/stable")
        self.requires.add("glib-networking/2.59.1@conanos/stable")
        self.requires.add("gmp/6.1.2-5@conanos/stable")
        self.requires.add("gnutls/3.5.19@conanos/stable")
        self.requires.add("graphene/1.8.2@conanos/stable")
        self.requires.add("gst-libav/1.14.4@conanos/stable")
        self.requires.add("gst-plugins-bad/1.14.4@conanos/stable")
        self.requires.add("gst-plugins-base/1.14.4@conanos/stable")
        self.requires.add("gst-plugins-good/1.14.4@conanos/stable")
        self.requires.add("gst-plugins-ugly/1.14.4@conanos/stable")
        self.requires.add("gst-rtsp-server/1.14.4@conanos/stable")
        self.requires.add("gstreamer/1.14.4@conanos/stable")
        self.requires.add("gtk-doc-lite/1.29@conanos/stable")
        self.requires.add("harfbuzz/2.1.3@conanos/stable")
        self.requires.add("json-glib/1.4.4@conanos/stable")
        self.requires.add("lame/3.100@conanos/stable")
        self.requires.add("libass/0.14.0-13@conanos/stable")
        self.requires.add("libbluray/1.0.2-3@conanos/stable")
        self.requires.add("libcdio/2.0.0@conanos/stable")
        self.requires.add("libcdio-paranoia/10.2-0.94-2-3@conanos/stable")
        self.requires.add("libcroco/0.6.12@conanos/stable")
        self.requires.add("libdca/0.0.6@conanos/stable")
        self.requires.add("libffi/3.299999@conanos/stable")
        self.requires.add("libgcrypt/1.8.4@conanos/stable")
        self.requires.add("libgpg-error/1.33@conanos/stable")
        self.requires.add("libiconv/1.15@conanos/stable")
        self.requires.add("libilbc/2.0.2-2@conanos/stable")
        self.requires.add("libkate/0.4.1@conanos/stable")
        self.requires.add("libnice/0.1.14@conanos/stable")
        self.requires.add("libogg/1.3.3@conanos/stable")
        self.requires.add("libpng/1.6.34@conanos/stable")
        self.requires.add("libpsl/0.20.2@conanos/stable")
        self.requires.add("librsvg/2.40.20@conanos/stable")
        self.requires.add("librtmp/2.4@conanos/stable")
        self.requires.add("libsoup/2.65.1@conanos/stable")
        self.requires.add("libsrtp/2.2.0@conanos/stable")
        self.requires.add("libssh/0.8.6@conanos/stable")
        self.requires.add("libtasn1/4.13@conanos/stable")
        self.requires.add("libtheora/1.1.1@conanos/stable")
        self.requires.add("libtiff/4.0.10@conanos/stable")
        self.requires.add("libvorbis/1.3.6@conanos/stable")
        self.requires.add("libvpx/1.7.0@conanos/stable")
        self.requires.add("libxml2/2.9.8@conanos/stable")
        self.requires.add("lzma/5.2.4@conanos/stable")
        self.requires.add("mfx_dispatch/1.27.r60@conanos/stable")
        self.requires.add("modplug/0.8.9.0.r274@conanos/stable")
        self.requires.add("mpg123/1.25.10@conanos/stable")
        self.requires.add("nettle/3.4.1@conanos/stable")
        self.requires.add("nv-codec-headers/n8.2.15.6@conanos/stable")
        self.requires.add("openh264/1.8.0@conanos/stable")
        self.requires.add("openjpeg/2.3.0@conanos/stable")
        self.requires.add("openssl/1.1.1@conanos/stable")
        self.requires.add("opus/1.2.1@conanos/stable")
        self.requires.add("orc/0.4.28@conanos/stable")
        self.requires.add("pango/1.42.4@conanos/stable")
        self.requires.add("pixman/0.34.0@conanos/stable")
        self.requires.add("soundtouch/2.1.2@conanos/stable")
        self.requires.add("soxr/0.1.3@conanos/stable")
        self.requires.add("spandsp/0.0.6@conanos/stable")
        self.requires.add("speex/1.2.0@conanos/stable")
        self.requires.add("sqlite3/3.21.0@conanos/stable")
        self.requires.add("taglib/1.11.1@conanos/stable")
        self.requires.add("wavpack/5.1.0@conanos/stable")
        self.requires.add("x264/0.152.r2854@conanos/stable")
        self.requires.add("x265/2.8@conanos/stable")
        self.requires.add("xvid/1.3.4-3@conanos/stable")
        self.requires.add("zlib/1.2.11@conanos/stable")


    def build(self):
        pass
        #gst_plugin_system_path_1_0 = ";".join( [ os.path.join(self.deps_cpp_info[lib].rootpath, "lib", "gstreamer-1.0") for lib in 
        #    ["gstreamer","gst-plugins-base","gst-plugins-good","gst-plugins-bad","gst-plugins-ugly","gst-rtsp-server","gst-libav"] ] )
        #pkg_config_path = ";".join([ os.path.join(libpath, "pkgconfig") for libpath in self.deps_cpp_info.lib_paths ])

        #replacements = {
        #    "%GST_PLUGIN_SYSTEM_PATH_1_0%" : gst_plugin_system_path_1_0,
        #    "%GSTREAMER%"                  : self.deps_cpp_info["gstreamer"].rootpath,
        #    "%GLIB_NETWORKING%"            : self.deps_cpp_info["glib-networking"].rootpath,
        #    "%PKG_CONFIG_PATH%"            : pkg_config_path,
        #    "%GST_PATH_1_0%"               : ";".join(self.deps_cpp_info.bin_paths),
        #}
        #tools.save(self.name+".bat", self.gst_bat)
        #for s, r in replacements.items():
        #    tools.replace_in_file(self.name+".bat", s,r,strict=True)

    def package(self):
        #self.copy(self.name+".bat", dst=os.path.join(self.package_folder),src=os.path.join(self.build_folder))
        #--------------------------------------------------------------
        for p in self.deps_cpp_info.rootpaths:
            tools.out.info("COPYING : " + p)
            self.copy("*", dst=self.package_folder, src=p, excludes=["conaninfo.txt","conanmanifest.txt","conanbuildinfo.txt"])
        #--------------------------------------------------------------
        gst_plugin_system_path_1_0 = os.path.join(self.package_folder, "lib", "gstreamer-1.0")
        pkg_config_path =  os.path.join(self.package_folder, "lib", "pkgconfig")
        replacements = {
            "%GST_PLUGIN_SYSTEM_PATH_1_0%" : gst_plugin_system_path_1_0,
            "%GSTREAMER%"                  : self.package_folder,
            "%GLIB_NETWORKING%"            : self.package_folder,
            "%PKG_CONFIG_PATH%"            : pkg_config_path,
            "%GST_PATH_1_0%"               : os.path.join(self.package_folder, "bin"),
        }
        tools.save(os.path.join(self.package_folder, self.name+".bat"), self.gst_bat)
        for s, r in replacements.items():
            tools.replace_in_file(os.path.join(self.package_folder, self.name+".bat"), s,r,strict=True)
        #---------------------------------------------------------------

    def package_info(self):
        pass


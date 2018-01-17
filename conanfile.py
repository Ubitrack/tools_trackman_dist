from conans import ConanFile
import os

class TrackmanConan(ConanFile):
    name = "ubitrack_tools_trackman"
    url = "https://github.com/Ubitrack/tools_trackman_dist.git"
    version = "1.0"
    build_policy = "missing"
    exports_sources = "bin/*", "doc/*", "lib/*"

    requires = (
        "java_installer/9.0.0@bincrafters/stable",
        "ubitrack_facade/[>=1.3.0]@ubitrack/stable",
        )

    def build(self):
      pass

    def package(self):
        self.copy("*", dst="", keep_path=True)

    def package_info(self):  
        self.output.info("Added Trackman Editor v%s" % self.version)
        self.env_info.TRACKMAN_BIN_PATH.append(os.path.join(self.package_folder, "bin"))
        self.env_info.TRACKMAN_LIB_PATH.append(os.path.join(self.package_folder, "lib"))

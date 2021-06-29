{ pkgs ? import <nixpkgs> {} }:

let
  raylib = pkgs.callPackage ./nix/raylib/default.nix {};
  mach-nix = import (builtins.fetchGit {
    url = "https://github.com/DavHau/mach-nix/";
    ref = "3.3.0";
  }) {};
  raylibpy = mach-nix.buildPythonPackage {
    src = builtins.fetchGit {
      url = "https://github.com/overdev/raylib-py";
      ref = "raylibpy-3.7";
      rev = "dc350971898f02194c2b8c896afe66a4b4fb56a0";
    };
  };
  raylibpy-flat = mach-nix.buildPythonPackage {
    src = builtins.fetchGit {
      url = "https://github.com/adamlwgriffiths/raylib-py-flat";
      ref = "master";
      rev = "58568e12e886823adb7f202391331a46b1b5951e";
    };
  };
  custom-python = mach-nix.mkPython {
    python = "python38";
    #requirements = builtins.readFile ./requirements.dev.txt;
    # include setuptools for deployments
    # explicit cffi required to avoid errors
    requirements = ''
      setuptools
      cffi>=1.12
      twine
      imgui
      PyOpenGL
      PyOpenGL_accelerate
    '';
    packagesExtra = [
      raylibpy
      raylibpy-flat
    ];
    providers = {
      _default = "nixpkgs,wheel,sdist";
      # fix for pyopengl not working from pypi
      # https://github.com/NixOS/nixpkgs/issues/76822
      PyOpenGL = "nixpkgs";
      PyOpenGL_accelerate = "nixpkgs";
      cffi = "nixpkgs";
    };
  };
in pkgs.mkShell {
  buildInputs = with pkgs; [
    raylib
    custom-python
  ];

  shellHook = ''
    export LD_LIBRARY_PATH="$(pwd)/lib:${raylib}/lib:$LD_LIBRARY_PATH"
    export RAYLIB_PATH=${raylib}
    export USE_EXTERNAL_RAYLIB=
  '';
}

{
    description = "bloons dev env";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
    pkgs = import nixpkgs { inherit system; };
    in {
      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs; [
          tesseract
          grim
          python314Packages.pytesseract
          python314Packages.evdev
          wtype
          wayland-utils
        ];
      };
    };
}

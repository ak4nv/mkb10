{
  description = "Flask Environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            gnumake
            uv
            sqlite
            wrk
          ];

          shellHook = ''
            # Pass pathes to the Nix libs into standard Linux linker
            export LD_LIBRARY_PATH="${pkgs.lib.makeLibraryPath (with pkgs; [
              # stdenv.cc.cc.lib
              # zlib
              # glib
              # openssl
              # zstd
            ])}:''$LD_LIBRARY_PATH"

            # Enable tip for activated environment
            export PS1="\[\e[1;36m\](dev)\[\e[0m\] ''$PS1"
            echo "Flask environment is ready for ${system}."
          '';
        };
      }
    );
}

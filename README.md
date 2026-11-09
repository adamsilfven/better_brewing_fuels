# Better Brewing Fuels

A lightweight Minecraft mod for brewing stands.

- **Charcoal:** 4 brewing operations per item.
- **Soul Sand:** 8 brewing operations per item.
- **Blaze Powder:** unchanged at its vanilla 20 operations.
- Supports the brewing stand fuel slot and hopper insertion.

## Porting status

This repository contains a **source candidate**, reconstructed from the supplied
Better Brewing Fuels 1.0 NeoForge 1.21.1 JAR. The original binary has **not**
been overwritten. No new loader builds should be treated as playable until
they compile successfully and pass in-game testing.

| Target | Status |
| --- | --- |
| NeoForge 1.21.1, original 1.0 | Original supplied separately; preserved |
| NeoForge 1.21.1, source 1.1.0 | GitHub Actions build passed; game tests pending |
| Fabric 1.21.1, source 1.1.0 | GitHub Actions build passed; game tests pending |
| Other Minecraft versions | Under investigation; see [VERSION_EXPANSION.md](VERSION_EXPANSION.md) |

## Project layout

- `shared/`: fuel rules and Minecraft Mixins shared by both loaders
- `fabric/`: Fabric Loom 1.21.1 project
- `neoforge/`: NeoForge ModDevGradle 1.21.1 project
- `tools/smoke_test.py`: limited Java compilation and fuel-rule tests using stubs
- `.github/workflows/build-1.21.1.yml`: CI build recipe for each loader

## Build

Both 1.21.1 loaders compiled successfully in [GitHub Actions run #2](https://github.com/adamsilfven/better_brewing_fuels/actions/runs/42687956383). These are **test candidates**, not game-verified releases. See [TESTING.md](TESTING.md).

Use GitHub **Actions**, workflow **Build both 1.21.1 loaders**. A successful run
uploads the distributable JARs as separate artifacts. Or on a Java 21 machine
with Gradle 8.14.4 and internet access:

```sh
python3 tools/smoke_test.py
gradle -p fabric clean build
gradle -p neoforge clean build
```

Only test production/remapped JARs, never `-dev` or `-sources` JARs.

## Required in-game acceptance

Test both loaders on 1.21.1, including brewing stand GUI insertion, hopper
insertion, Charcoal = 4 charges, Soul Sand = 8 charges, Blaze Powder = 20,
incorrect items rejected, stack conservation, dedicated server behavior,
persistence after restart and representative modpack compatibility.
Mixin injection targets must be reviewed separately for every new game version.

The intended logic is server-side, but install the mod on **client and server**
for dependable inventory/GUI behavior. No Fabric API dependency is needed.

## Version support

See [VERSION_EXPANSION.md](VERSION_EXPANSION.md). Separate tested binaries
are required for different loaders and Minecraft internals.

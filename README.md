# Better Brewing Fuels

A lightweight Minecraft mod for brewing stands.

- **Charcoal:** 4 brewing operations per item.
- **Soul Sand:** 8 brewing operations per item.
- **Blaze Powder:** unchanged at its vanilla 20 operations.
- Supports the brewing stand fuel slot and hopper insertion.

## Porting status

Version 1.1.0 has been built for all three loaders on Minecraft 1.21.1.
**The mod author confirmed that all three builds passed in-game testing on November 9, 2026.**
The original NeoForge 1.0 binary was not overwritten. The scope of game
verification beyond that author confirmation is not independently documented.

| Target | Status |
| --- | --- |
| NeoForge 1.21.1, original 1.0 | Original supplied separately; preserved |
| NeoForge 1.21.1, source 1.1.0 | GitHub Actions build passed; author-confirmed in-game PASS |
| Fabric 1.21.1, source 1.1.0 | GitHub Actions build passed; author-confirmed in-game PASS |
| Forge 1.21.1, source 1.1.0 | GitHub Actions build passed; author-confirmed in-game PASS |
| Fabric 1.20.1 | GitHub Actions build passed; author-confirmed in-game PASS |
| Forge 1.20.1 | Corrected RC2 passed CI and author-confirmed in-game PASS; stable release published |
| Other Minecraft versions | Under investigation; see [VERSION_EXPANSION.md](VERSION_EXPANSION.md) |

## Project layout

- `shared/`: fuel rules and Mixins shared by Fabric and NeoForge
- `fabric/`: Fabric Loom 1.21.1 project
- `neoforge/`: NeoForge ModDevGradle 1.21.1 project
- `forge/`: ForgeGradle 7 1.21.1 project (CI and author-reported in-game PASS)
- `ports/1.20.1/fabric/`: Java 17 Fabric 1.20.1 port (CI and author-reported game PASS)
- `ports/1.20.1/forge/`: Java 17 Forge 1.20.1 SRG port (RC2 CI and author-reported in-game PASS)
- `tools/smoke_test.py`: limited Java compilation and fuel-rule tests using stubs
- `.github/workflows/build-1.21.1.yml`: Fabric and NeoForge CI build workflow
- `.github/workflows/build-forge-1.21.1.yml`: Forge CI build workflow

## Downloads

- **Stable Minecraft 1.21.1:** [v1.1.0](https://github.com/adamsilfven/better_brewing_fuels/releases/tag/v1.1.0) (all three loaders; author reports in-game PASS)
- **Stable Minecraft 1.20.1:** [v1.1.0-mc1.20.1](https://github.com/adamsilfven/better_brewing_fuels/releases/tag/v1.1.0-mc1.20.1) (Fabric and Forge both author-confirmed in-game PASS). The earlier RC1 Forge JAR is broken and superseded.

## Build

Forge is built separately by the [Forge 1.21.1 workflow](.github/workflows/build-forge-1.21.1.yml) using Gradle 9.3.0. It passed CI and the mod author's in-game test.

Fabric and NeoForge compiled successfully in [GitHub Actions run #2](https://github.com/adamsilfven/better_brewing_fuels/actions/runs/42687956383); Forge compiled successfully in [the clean Forge run](https://github.com/adamsilfven/better_brewing_fuels/actions/runs/42697496779). The mod author confirmed all three function in-game. Download the direct JAR assets from the [v1.1.0 GitHub Release](https://github.com/adamsilfven/better_brewing_fuels/releases/tag/v1.1.0); see [TESTING.md](TESTING.md).

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

Before distributing to large packs, test each loader on 1.21.1, including brewing stand GUI insertion, hopper
insertion, Charcoal = 4 charges, Soul Sand = 8 charges, Blaze Powder = 20,
incorrect items rejected, stack conservation, dedicated server behavior,
persistence after restart and representative modpack compatibility.
Mixin injection targets must be reviewed separately for every new game version.

The intended logic is server-side, but install the mod on **client and server**
for dependable inventory/GUI behavior. No Fabric API dependency is needed.

## Version support

See [VERSION_EXPANSION.md](VERSION_EXPANSION.md). Separate tested binaries
are required for different loaders and Minecraft internals.

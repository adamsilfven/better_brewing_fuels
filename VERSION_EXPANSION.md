# Minecraft version expansion investigation (November 9, 2026)

## Findings

1. The fuel math and intent are portable; Minecraft internals are not.
   The game uses obfuscated/intermediary mappings through 1.21.11 for Fabric,
   while 26.1+ runs with Mojang's unobfuscated names. The 26.x releases
   require Java 25, whereas 1.21.x needs Java 21.
2. Brewing stand implementation and the exact mixin targets (`serverTick`,
   `canPlaceItem`, `mayPlaceItem`, constant 20 and `ItemStack.is(Item)`)
   require inspection **per version**, even when the target compiles.
3. 1.20.1 is strategically valuable, but requires an additional Forge target.
   NeoForge does exist for 1.20.1, but its maintainers recommend Forge for it.
   Java 17 for both loaders on 1.20.1.
4. Do not assume one Minecraft release family shares binary compatibility.
5. A single JAR cannot be safely declared compatible with all versions. Ship
   separate, tested artifacts by loader/version family. Share code and tests.

## Suggested release waves

| Wave | Minecraft versions | Loader targets | Key work |
| --- | --- | --- | --- |
| 1 | 1.21.1 | Fabric, NeoForge | Finish CI, mappings and full game tests |
| 2 | 1.20.1 | Fabric, Forge | Java 17, API/mapping adjustments, test mixins |
| 3 | 1.21.4 / 1.21.5 / 1.21.8 / 1.21.11 | Fabric, NeoForge where supported | Group versions by verified method signatures, not advertised ranges |
| 4 | 26.1.2 / 26.2 / 26.3 | Fabric, NeoForge | Java 25, 26.x toolchain and APIs |
| Later | 1.19.2, 1.18.2 and older | Fabric, Forge where maintained | Additional source forks; assess demand |

## Maintainable structure

- Retain `shared/` for fuel values, shared Mixin classes (when signatures match),
  and automated fuel behavior tests.
- Maintain separately pinned Gradle subprojects for each *verified* Minecraft
  class/API family. Split mixins into version-scoped source where required.
- Use GitHub Actions matrix to build and upload each variant.
- Add automated launch/functional tests with GameTest where supported.
- Keep mod ID stable. Artifact filenames should include loader and game version.
- Don't claim Quilt unless tested. Don't conflate server-side logic with
  client-only installation.

## Relevant public documentation

- Fabric mappings and remapping:
  https://docs.fabricmc.net/develop/loom/
- NeoForge ModDevGradle:
  https://github.com/NeoForgeMDKs/MDK-1.21.1-ModDevGradle
- NeoForge loader version coverage:
  https://docs.neoforged.net/user/docs/
- Minecraft version numbering:
  https://www.minecraft.net/en-us/article/minecraft-new-version-numbering-system
- Minecraft 26.x mapping transition:
  https://fabricmc.net/2026/03/14/261.html

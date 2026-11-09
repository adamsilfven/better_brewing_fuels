# Minecraft version expansion plan (November 9, 2026)

## Confirmed release

**Minecraft 1.21.1**: Fabric, NeoForge and Forge builds have passed GitHub Actions compilation, and the mod author reports all three passed in-game testing. These files remain available unchanged in [stable v1.1.0](https://github.com/adamsilfven/better_brewing_fuels/releases/tag/v1.1.0).

## Additional versions

| Target | Loaders | Java | Status / technical considerations |
| --- | --- | --- | --- |
| 1.20.1 | Fabric + Forge | 17 | In progress under `ports/1.20.1/`; needs loader-specific remapping and in-game acceptance |
| 26.3 | Fabric + NeoForge + Forge where supported | 25 | Research complete; new `brewing_fuel` item component permits avoiding the historical Mixins |
| 1.21.4, 1.21.5, 1.21.8, 1.21.11 | Fabric, NeoForge, Forge where supported | 21 | Compile and validate separate class/API families; don't infer cross-patch compatibility |
| 26.2, 26.1.2 | Supported mod loaders | 25 | Check each version's brewing fuel implementation and loader API |
| 1.19.2, 1.18.2 | Fabric + Forge | 17 | Older source branches and compatibility tests |
| 1.16.5 | Fabric + Forge | 8 | Much older Java, Gradle and Mixin dependencies; only if demand warrants |

## Important technical distinctions

- A Minecraft version or loader change can alter class names, methods, Mixin injection points and obfuscation mappings. **One universal JAR is not a safe release strategy.**
- Fabric on Minecraft **1.21.11 and older** requires remapping to intermediary names; modern Fabric on **26.1+** uses unobfuscated official names and a different Loom plugin.
- Forge on Minecraft **1.20.4 and older** requires production renaming, with an embedded Mixin reference map when using remapped Mixins. In Minecraft 1.21.1, the project uses the Mojang-mapped runtime directly.
- Minecraft **26.3** introduced `DataComponents.BREWING_FUEL` with `uses` and `speed_multiplier` fields. Its **Fabric API `DefaultItemComponentEvents`** can modify the default components on vanilla Charcoal and Soul Sand directly. Loader-specific events or components are preferable to altering the brewing stand tick function, when available.
- NeoForge exists for 1.20.1 but its own documentation recommends **Forge for 1.20.1**, so the initial 1.20.1 port targets Fabric and Forge.
- Keep the mod ID `brewing_fuel_expansion` and exact accepted fuel values: Charcoal=4, Soul Sand=8, Blaze Powder=20.
- Avoid changing stable 1.21.1 binaries while adding ports. Stage new builds as candidates and secure in-game acceptance before a stable release.

## Acceptance requirements

For every unique version/loader binary, test Minecraft startup/world load, fuel GUI insertion, one item of each fuel giving **exactly** 4/8/20 operations, shift-clicking, hopper automation, stacks, save/reload persistence, and dedicated server when possible. A green Gradle run proves compilation, **not gameplay behavior**.

## Sources

- [Fabric Loom documentation](https://docs.fabricmc.net/develop/loom/)
- [Fabric mappings migration guide](https://docs.fabricmc.net/develop/porting/mappings/index)
- [Fabric 26.3 porting announcement](https://fabricmc.net/2026/09/15/263.html)
- [Mojang 26.3 notes, brewing fuel component](https://feedback.minecraft.net/hc/en-us/articles/48913133328013-Minecraft-Java-Edition-26-3)
- [Minecraft Forge MDK remapped Mixins example](https://github.com/MinecraftForge/MDKExamples/tree/master/mixins-obfuscation/fg7)
- [Forge 1.20.1 download/version history](https://files.minecraftforge.net/net/minecraftforge/forge/index_1.20.1.html)
- [NeoForge note about 1.20.1](https://docs.neoforged.net/user/docs/)

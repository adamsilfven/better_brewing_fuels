# Forge 1.21.1 test candidate

This is a distinct mod loader build, **not** the existing NeoForge JAR.
Requires Minecraft 1.21.1, Java 21 and Minecraft Forge 52.1.21
(for initial CI verification).

The loader adapter uses official Mojang mappings, ForgeGradle 7 and
Forge's `mods.toml` metadata, and loads the shared brewing Mixins via
the JAR's `MixinConfigs` manifest attribute.

## Build

Run the [Build Forge 1.21.1](../.github/workflows/build-forge-1.21.1.yml)
GitHub Actions workflow or use Java 21 and Gradle 9.3.0:

```sh
gradle -p forge clean build
```

A successful compile **does not confirm** that all injection points
work at runtime. Test in a clean Forge profile first, checking Charcoal
(4 fuel), Soul Sand (8), Blaze Powder (20), GUI slot, hopper, persistence,
and dedicated server. Do not combine with Fabric or NeoForge JARs.

# Better Brewing Fuels 1.1.0: 1.21.1 Acceptance Checklist

**Acceptance reported November 9, 2026:** The mod author confirmed that the Fabric, NeoForge and Forge 1.21.1 JARs all passed in-game testing. Fabric and NeoForge builds passed [CI run #2](https://github.com/adamsilfven/better_brewing_fuels/actions/runs/42687956383); Forge passed [CI](https://github.com/adamsilfven/better_brewing_fuels/actions/runs/42697496779). This is author-reported acceptance; dedicated server and broader modpack coverage remain undocumented.

## Regression checklist for future versions (keep your working installation unchanged)

1. Create a clean Minecraft **1.21.1 Fabric** profile with Fabric Loader; put ONLY `better-brewing-fuels-fabric-1.21.1-1.1.0.jar` in its mods folder.
2. Create a separate clean Minecraft **1.21.1 NeoForge 21.1.259+** profile; put ONLY `better-brewing-fuels-neoforge-1.21.1-1.1.0.jar` in its mods folder. Don't install both JARs together.
3. Create a separate clean Minecraft **1.21.1 Forge 52.1.21** profile with ONLY the Forge 1.21.1 JAR. Never combine loader JARs.
4. Verify the game reaches the main menu and a world loads with no Mixin errors.
5. With a brewing stand and potion ingredients, insert **one Charcoal** in the fuel slot. Check it gives **4** charges; one full brewing cycle consumes one charge.
6. Repeat with **one Soul Sand**. Check it gives **8** charges. Soul Soil should **not** count.
7. Confirm **Blaze Powder** still provides **20** charges.
8. Check the fuels can be placed in the fuel GUI slot but not in the ingredient or bottle slots.
9. Test hopper insertion into the brewing stand and verify no duplication or item loss with stacks.
10. Save/reopen the world with unused charges; verify fuel persists.
11. Repeat on a dedicated server with the mod installed on both client and server. Test a representative modpack last.

## How to download JARs

Download the loader-specific JAR directly from [GitHub Releases v1.1.0](https://github.com/adamsilfven/better_brewing_fuels/releases/tag/v1.1.0):
- `better-brewing-fuels-fabric-1.21.1-1.1.0.jar`
- `better-brewing-fuels-neoforge-1.21.1-1.1.0.jar`
- `better-brewing-fuels-forge-1.21.1-1.1.0.jar`

These direct downloads do not require extracting an Actions artifact ZIP.

## Reporting a problem

Include: Minecraft version, loader/version, the relevant JAR filename,
whether failure is during startup or brewing, `latest.log`, and reproduction
steps. Avoid replacing an existing working pack's JAR until the new file is accepted.

All three loader builds are author-accepted for Minecraft 1.21.1; continue to test future versions and broader deployment scenarios independently.

## Minecraft 1.20.1 acceptance (stable)

A separate Fabric + Forge source port is available under `ports/1.20.1/`.
They are a **separate stable release** for Minecraft 1.20.1; do not use them in Minecraft 1.21.1.

- **Fabric 1.20.1 PASS (author-reported):** Minecraft loaded and mod worked. The accepted RC1 Fabric binary was carried into RC2 byte-for-byte.
- **Forge 1.20.1 RC1 FAILED:** author reported the `failed to load a valid ResourcePackInfo` warning at startup. Inspection confirmed the `pack.mcmeta` file was absent. Do not use RC1 Forge.
- **Forge 1.20.1 RC2 PASS (author-reported, November 9, 2026):** The author confirmed the corrected JAR works in-game. `pack.mcmeta` (format 15) fixes the prior startup warning. Fresh CI compilation and archive checks passed, including the SRG Mixin reference map.
- Download the **unchanged, accepted JARs** from [the stable Minecraft 1.20.1 release](https://github.com/adamsilfven/better_brewing_fuels/releases/tag/v1.1.0-mc1.20.1). Both loaders are author-confirmed in-game PASS.
- **Ongoing regression checklist:** Use only one JAR for the matching 1.20.1 loader. Verify Charcoal = 4, Soul Sand = 8, Blaze Powder = 20, **including one-item stacks**, plus fuel GUI, hoppers, save/reload and dedicated server when possible. Dedicated-server and broad modpack acceptance have not been independently documented.
- Never replace a 1.21.1 JAR with a 1.20.1 JAR or install both loaders together.


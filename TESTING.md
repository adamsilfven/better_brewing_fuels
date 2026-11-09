# Better Brewing Fuels 1.1.0: 1.21.1 Acceptance Checklist

Both GitHub Actions compilation jobs passed in [run #2](https://github.com/adamsilfven/better_brewing_fuels/actions/runs/42687956383). **This does not mean in-game testing has passed.**

## Test profiles (keep your working installation unchanged)

1. Create a clean Minecraft **1.21.1 Fabric** profile with Fabric Loader; put ONLY `better-brewing-fuels-fabric-1.21.1-1.1.0.jar` in its mods folder.
2. Create a separate clean Minecraft **1.21.1 NeoForge 21.1.259+** profile; put ONLY `better-brewing-fuels-neoforge-1.21.1-1.1.0.jar` in its mods folder. Don't install both JARs together.
3. Verify the game reaches the main menu and a world loads with no Mixin errors.
4. With a brewing stand and potion ingredients, insert **one Charcoal** in the fuel slot. Check it gives **4** charges; one full brewing cycle consumes one charge.
5. Repeat with **one Soul Sand**. Check it gives **8** charges. Soul Soil should **not** count.
6. Confirm **Blaze Powder** still provides **20** charges.
7. Check the fuels can be placed in the fuel GUI slot but not in the ingredient or bottle slots.
8. Test hopper insertion into the brewing stand and verify no duplication or item loss with stacks.
9. Save/reopen the world with unused charges; verify fuel persists.
10. Repeat on a dedicated server with the mod installed on both client and server. Test a representative modpack last.

## How to download JARs

From the [successful GitHub Actions run](https://github.com/adamsilfven/better_brewing_fuels/actions/runs/42687956383), choose the matching artifact:
- `better-brewing-fuels-fabric-1.21.1`
- `better-brewing-fuels-neoforge-1.21.1`

Download and unzip each artifact, then use the lone JAR inside.

## Reporting a problem

Include: Minecraft version, loader/version, the relevant JAR filename,
whether failure is during startup or brewing, `latest.log`, and reproduction
steps. Avoid replacing an existing working pack's JAR until the new file is accepted.

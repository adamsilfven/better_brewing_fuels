#!/usr/bin/env python3
"""Verify that the shipped 1.20.1 Forge JAR has a loadable resource pack and Mixin metadata."""
import json
import pathlib
import sys
import zipfile

jar_path = pathlib.Path(sys.argv[1])
if not jar_path.is_file():
    raise SystemExit(f"Missing expected Forge JAR: {jar_path}")

with zipfile.ZipFile(jar_path) as archive:
    bad_file = archive.testzip()
    assert bad_file is None, f"Corrupted ZIP entry: {bad_file}"
    entries = set(archive.namelist())
    print(f"Inspecting production Forge JAR: {jar_path} ({len(entries)} entries)")
    print("Entries:", ", ".join(sorted(entries)), flush=True)
    required = (
        "META-INF/mods.toml",
        "pack.mcmeta",
        "brewing_fuel_expansion.1201.mixins.json",
        "brewing_fuel_expansion.1201.refmap.json",
        "com/adamsilfven/brewingfuel/Fuels.class",
        "com/adamsilfven/brewingfuel/mixin1201/BrewingStand1201Mixin.class",
        "com/adamsilfven/brewingfuel/mixin1201/FuelSlot1201Mixin.class",
    )
    for entry in required:
        assert entry in entries, f"Required Forge JAR entry missing: {entry}"
        print(f"PASS: {entry}")
    pack = json.loads(archive.read("pack.mcmeta").decode("utf-8"))["pack"]
    assert pack.get("pack_format") == 15, f"Unexpected pack_format: {pack.get('pack_format')!r}"
    assert isinstance(pack.get("description"), str) and pack["description"].strip(), "Missing pack description"
    print("PASS: pack.mcmeta is valid JSON and has Minecraft 1.20.1 resource-pack format 15")
    mixins = json.loads(archive.read("brewing_fuel_expansion.1201.mixins.json"))
    assert mixins["refmap"] == "brewing_fuel_expansion.1201.refmap.json"
    assert set(mixins["mixins"]) == {"BrewingStand1201Mixin", "FuelSlot1201Mixin"}
    json.loads(archive.read("brewing_fuel_expansion.1201.refmap.json"))
    print("PASS: Mixin config and reference map are present and parseable")
    mods_toml = archive.read("META-INF/mods.toml").decode("utf-8")
    assert 'modId="brewing_fuel_expansion"' in mods_toml
    assert 'versionRange="[1.20.1,1.20.2)"' in mods_toml
    assert 'versionRange="[47.4,48)"' in mods_toml
    print("PASS: Forge mod metadata targets Minecraft 1.20.1 and Forge 47.4.x")
    manifest = archive.read("META-INF/MANIFEST.MF").decode("utf-8")
    assert "MixinConfigs: brewing_fuel_expansion.1201.mixins.json" in manifest
    print("PASS: Forge manifest activates the Mixin config")
    cls = archive.read("com/adamsilfven/brewingfuel/Fuels.class")
    assert cls[:4] == bytes.fromhex("cafebabe"), "Not a compiled Java class"
    assert int.from_bytes(cls[6:8], "big") == 61, "Expected Java 17 bytecode (major 61)"
    print("PASS: Shared fuel logic uses Java 17 bytecode")

print("PASS: Forge 1.20.1 artifact archive and resource-pack metadata verified")

from pathlib import Path
import tempfile, subprocess
root = Path(__file__).resolve().parent.parent
with tempfile.TemporaryDirectory() as temp:
 base = Path(temp)
 stubs = {
 'net/minecraft/world/item/Item.java': 'package net.minecraft.world.item; public class Item {}',
 'net/minecraft/world/item/Items.java': 'package net.minecraft.world.item; public class Items { public static final Item CHARCOAL=new Item(), SOUL_SAND=new Item(), BLAZE_POWDER=new Item(), DIRT=new Item(); }',
 'net/minecraft/world/item/ItemStack.java': 'package net.minecraft.world.item; public class ItemStack { private final Item item; public ItemStack(Item item){this.item=item;} public boolean is(Item other){return item==other;} }',
 'net/minecraft/core/BlockPos.java': 'package net.minecraft.core; public class BlockPos {}',
 'net/minecraft/world/level/Level.java': 'package net.minecraft.world.level; public class Level {}',
 'net/minecraft/world/level/block/state/BlockState.java': 'package net.minecraft.world.level.block.state; public class BlockState {}',
 'net/minecraft/world/level/block/entity/BrewingStandBlockEntity.java': 'package net.minecraft.world.level.block.entity; import net.minecraft.world.item.ItemStack; public class BrewingStandBlockEntity { public ItemStack getItem(int slot){ return null; } }',
 'net/neoforged/fml/common/Mod.java': 'package net.neoforged.fml.common; import java.lang.annotation.*; @Retention(RetentionPolicy.RUNTIME) public @interface Mod {String value();}',
 'org/spongepowered/asm/mixin/Mixin.java': 'package org.spongepowered.asm.mixin; public @interface Mixin {Class<?>[] value() default {}; String[] targets() default {};}',
 'org/spongepowered/asm/mixin/injection/At.java': 'package org.spongepowered.asm.mixin.injection; public @interface At { String value(); String target() default ""; int ordinal() default -1;}',
 'org/spongepowered/asm/mixin/injection/Constant.java': 'package org.spongepowered.asm.mixin.injection; public @interface Constant { int intValue();}',
 'org/spongepowered/asm/mixin/injection/Redirect.java': 'package org.spongepowered.asm.mixin.injection; public @interface Redirect {String method(); At at();}',
 'org/spongepowered/asm/mixin/injection/ModifyConstant.java': 'package org.spongepowered.asm.mixin.injection; public @interface ModifyConstant {String method(); Constant constant();}',
 'org/spongepowered/asm/mixin/injection/Inject.java': 'package org.spongepowered.asm.mixin.injection; public @interface Inject {String method(); At at(); boolean cancellable() default false;}',
 'org/spongepowered/asm/mixin/injection/callback/CallbackInfoReturnable.java': 'package org.spongepowered.asm.mixin.injection.callback; public class CallbackInfoReturnable<T> { public void setReturnValue(T v){} }',
 'Tests.java': """import com.adamsilfven.brewingfuel.Fuels;
import net.minecraft.world.item.*;
public class Tests {
 public static void main(String[] args) {
  verify("Charcoal",new ItemStack(Items.CHARCOAL),4);
  verify("Soul Sand",new ItemStack(Items.SOUL_SAND),8);
  verify("Blaze Powder remains vanilla",new ItemStack(Items.BLAZE_POWDER),0);
  verify("Ordinary items rejected",new ItemStack(Items.DIRT),0);
  System.out.println("PASS: 4 portable fuel logic checks; all Java sources compiled against local stubs");
 }
 static void verify(String name,ItemStack i,int count){
  if(Fuels.extraCharges(i)!=count) throw new IllegalStateException(name+":"+Fuels.extraCharges(i)+" != "+count);
 }
}""",
 }
 for rel,s in stubs.items():
  p=base/rel; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(s)
 sources=[str(p) for p in base.rglob('*.java')]+[str(p) for p in (root/'shared/src/main/java').rglob('*.java')]+[str(p) for p in (root/'neoforge/src/main/java').rglob('*.java')]
 build=base/'out'; build.mkdir()
 p=subprocess.run(['javac','-encoding','UTF-8','--release','21','-d',str(build),*sources],capture_output=True,text=True)
 print('JAVAC',p.returncode,p.stdout,p.stderr)
 assert p.returncode==0
 p=subprocess.run(['java','-cp',str(build),'Tests'],capture_output=True,text=True)
 print('JAVA_TEST',p.returncode,p.stdout,p.stderr)
 assert p.returncode==0

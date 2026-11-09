package com.adamsilfven.brewingfuel.mixin1201;

import com.adamsilfven.brewingfuel.Fuels;
import net.minecraft.core.BlockPos;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.entity.BrewingStandBlockEntity;
import net.minecraft.world.level.block.state.BlockState;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Constant;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.ModifyConstant;
import org.spongepowered.asm.mixin.injection.Redirect;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

/** Mojmap source remapped by Fabric Loom to 1.20.1 intermediary at packaging time. */
@Mixin(BrewingStandBlockEntity.class)
public abstract class BrewingStand1201Mixin {
    @Redirect(method = "serverTick", at = @At(value = "INVOKE",
        target = "Lnet/minecraft/world/item/ItemStack;is(Lnet/minecraft/world/item/Item;)Z", ordinal = 0))
    private static boolean betterBrewingFuels$accept(ItemStack stack, Item item) {
        return stack.is(item) || Fuels.extraCharges(stack) > 0;
    }

    @ModifyConstant(method = "serverTick", constant = @Constant(intValue = 20))
    private static int betterBrewingFuels$chargeCount(int original,
            Level level, BlockPos pos, BlockState state, BrewingStandBlockEntity stand) {
        int value = Fuels.extraCharges(stand.getItem(4));
        return value > 0 ? value : original;
    }

    @Inject(method = "canPlaceItem", at = @At("HEAD"), cancellable = true)
    private void betterBrewingFuels$hopper(int slot, ItemStack stack,
            CallbackInfoReturnable<Boolean> cir) {
        if (slot == 4 && Fuels.extraCharges(stack) > 0) cir.setReturnValue(true);
    }
}

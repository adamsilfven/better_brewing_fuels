package com.adamsilfven.brewingfuel.forgemixin;

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

/** Forge 1.21.1 uses Mojang method names for these injection targets. */
@Mixin(value = BrewingStandBlockEntity.class, remap = false)
public abstract class BrewingStandForgeMixin {

    @Redirect(method = "serverTick", at = @At(value = "INVOKE",
        target = "Lnet/minecraft/world/item/ItemStack;is(Lnet/minecraft/world/item/Item;)Z",
        ordinal = 0, remap = false), remap = false)
    private static boolean brewingFuelExpansion$acceptFuel(ItemStack stack, Item originalFuel) {
        return stack.is(originalFuel) || Fuels.extraCharges(stack) > 0;
    }

    @ModifyConstant(method = "serverTick", constant = @Constant(intValue = 20), remap = false)
    private static int brewingFuelExpansion$charges(int originalCharges,
            Level level, BlockPos pos, BlockState state, BrewingStandBlockEntity stand) {
        int extra = Fuels.extraCharges(stand.getItem(4));
        return extra > 0 ? extra : originalCharges;
    }

    @Inject(method = "canPlaceItem", at = @At("HEAD"), cancellable = true, remap = false)
    private void brewingFuelExpansion$automation(int slot, ItemStack stack,
            CallbackInfoReturnable<Boolean> callback) {
        if (slot == 4 && Fuels.extraCharges(stack) > 0) {
            callback.setReturnValue(true);
        }
    }
}

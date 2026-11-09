package com.adamsilfven.brewingfuel.forgemixin;

import com.adamsilfven.brewingfuel.Fuels;
import net.minecraft.world.item.ItemStack;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

@Mixin(targets = "net.minecraft.world.inventory.BrewingStandMenu$FuelSlot", remap = false)
public abstract class FuelSlotForgeMixin {
    @Inject(method = "mayPlaceItem", at = @At("HEAD"), cancellable = true, remap = false)
    private static void brewingFuelExpansion$slot(ItemStack stack,
            CallbackInfoReturnable<Boolean> callback) {
        if (Fuels.extraCharges(stack) > 0) {
            callback.setReturnValue(true);
        }
    }
}

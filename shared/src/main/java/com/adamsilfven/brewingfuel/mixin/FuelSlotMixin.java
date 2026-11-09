package com.adamsilfven.brewingfuel.mixin;

import com.adamsilfven.brewingfuel.Fuels;
import net.minecraft.world.item.ItemStack;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

/** The brewing stand GUI fuel slot must accept the same items as automation. */
@Mixin(targets = "net.minecraft.world.inventory.BrewingStandMenu$FuelSlot")
public abstract class FuelSlotMixin {
    @Inject(method = "mayPlaceItem", at = @At("HEAD"), cancellable = true)
    private static void brewingFuelExpansion$slot(ItemStack stack,
            CallbackInfoReturnable<Boolean> callback) {
        if (Fuels.extraCharges(stack) > 0) {
            callback.setReturnValue(true);
        }
    }
}

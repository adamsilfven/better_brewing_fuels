package com.adamsilfven.brewingfuel.mixin1201;

import com.adamsilfven.brewingfuel.Fuels;
import net.minecraft.world.item.ItemStack;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

@Mixin(targets = "net.minecraft.world.inventory.BrewingStandMenu$FuelSlot")
public abstract class FuelSlot1201Mixin {
    @Inject(method = "mayPlace", at = @At("HEAD"), cancellable = true)
    private void betterBrewingFuels$slot(ItemStack stack, CallbackInfoReturnable<Boolean> cir) {
        if (Fuels.extraCharges(stack) > 0) cir.setReturnValue(true);
    }
}

package com.adamsilfven.brewingfuel;

import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;

/** Exact fuel values from the supplied 1.0 NeoForge binary. */
public final class Fuels {
    private Fuels() { }

    public static int extraCharges(ItemStack stack) {
        if (stack.is(Items.CHARCOAL)) return 4;
        if (stack.is(Items.SOUL_SAND)) return 8;
        return 0;
    }
}

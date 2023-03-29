#############################
#                           #
#          1.12.2           #
#                           #
#############################
##loader contenttweaker
#import mods.contenttweaker.VanillaFactory;
#import mods.contenttweaker.Item;

#VMCN ITEM
#val vmcn_item as Item = VanillaFactory.createItem("vmcn_item");
#vmcn_item.maxDamage = 114514;
#vmcn_item.rarity = "rare";
#vmcn_item.creativeTab = <creativetab:tools>;
#vmcn_item.toolClass = "pickaxe";
#vmcn_item.toolLevel = 1919810;
#vmcn_item.beaconPayment = true;
#vmcn_item.register();
#recipes.addShaped(<ccontenttweaker:vmcn_item>,
# [[<vm:yi_qv>, <vm:KaCarl19>, <vm:oaktree233>],
# [<vm:YiChenSamaaaaaaaaaa>, <vm:3093FengMing>, <vm:KlparetlR>],
# [<vm:nageih>, <vm:QingLanono>, <vm:Wulian233>]]);

#############################
#                           #
#          1.18.2           #
#                           #
#############################
#VMCN ITEM
##loader contenttweaker
#import mods.contenttweaker.item.ItemBuilder;
#import mods.contenttweaker.item.tool.ItemBuilderTool;
#import crafttweaker.api.food.MCFood;
#new ItemBuilder()
#    .withMaxStackSize(114514)
#    .isImmuneToFire()
#    .build("vmcn_item");
#craftingTable.addShaped("vmcn_item_craft", <ccontenttweaker:vmcn_item>,
# [[<vm:yi_qv>, <vm:KaCarl19>, <vm:oaktree233>],
# [<vm:YiChenSamaaaaaaaaaa>, <vm:3093FengMing>, <vm:KlparetlR>],
# [<vm:nageih>, <vm:QingLanono>, <vm:Wulian233>]]);
#<item:ccontenttweaker:vmcn_item>.addTooltip("希望这个小圈子越来越好");
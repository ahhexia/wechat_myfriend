import uiautomator2 as u2

d = u2.connect("rozl5xwgmbq8toaa")
# print(d.info)
# d.app_start("com.tencent.mm")
# d.wait_activity(".ui.LauncherUI",timeout=10)
# d(text="通讯录").click()
# d.unlock()
xml = d.dump_hierarchy()
# print(xml)
with open(r"dumps\shanchu.uix","wt",encoding="utf-8") as file:
    file.write(xml)

im = d.screenshot()
im.save(r"dumps\shanchu.png")

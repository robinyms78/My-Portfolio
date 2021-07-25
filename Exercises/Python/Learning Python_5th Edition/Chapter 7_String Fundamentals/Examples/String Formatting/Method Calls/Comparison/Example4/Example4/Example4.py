# Hardcoded references in both
import sys

# print("My {1[kind]: < 8} runs {0.platform: > 8}".format(sys, {"kind":"laptop"}))
print("My %(kind)-8s runs %(plat)8s" %dict(kind = "laptop", plat = sys.platform))

# Building data ahead of time in both
data = dict(platform = sys.platform, kind = "laptop")
# print("My {kind: < 8} runs {platform: > 8}".format(**data))
print("My %(kind)-8s runs %(platform)8s" %data)
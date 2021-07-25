import sys
print("My {1[kind]} runs {0.platform}".format(sys, {"kind": "laptop"}))
print("My {map[kind]} runs {sys.platform}".format(sys = sys, map = {"kind": "laptop"}))



def _sinusoid_():
    h, m, s = map(int, input().split())
	angle = (h * 3600 + m * 60 + s) / 120
	print(f"Angle: {angle:}")

if __name__ == "__main__":
    _sinusoid_()
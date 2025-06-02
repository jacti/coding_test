def draw_circles_svg(circle_data, scale=50):
    """
    circle_data: 리스트 [(x, r), ...]
    scale: 확대 배율 (기본 50배)
    """
    padding = 0.2 * scale  # 확대된 패딩
    svg_elements = []

    # 모든 원의 y좌표는 0 (수평선 위)
    max_radius = max(r for _, r in circle_data)
    max_x = max(x + r for x, r in circle_data)
    min_x = min(x - r for x, r in circle_data)

    width = int((max_x - min_x) * scale + 2 * padding)
    height = int(max_radius * 2 * scale + 2 * padding)

    svg_header = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
    svg_footer = '</svg>'
    
    center_y = padding + max_radius * scale

    # 수평선
    svg_elements.append(
        f'<line x1="0" y1="{center_y}" x2="{width}" y2="{center_y}" stroke="black" stroke-width="2"/>'
    )

    # 원들
    for x, r in circle_data:
        cx = (x - min_x) * scale + padding
        radius = r * scale
        svg_elements.append(
            f'<circle cx="{cx}" cy="{center_y}" r="{radius}" stroke="blue" stroke-width="2" fill="none" />'
        )

    svg_content = svg_header + "\n".join(svg_elements) + "\n" + svg_footer
    return svg_content


# 예제 입력 처리
input_data = """
8
5 5
2 2
7 3
1 1
3 1
9 1
6 2
16 4
"""

lines = input_data.strip().split('\n')
n = int(lines[0])
circles = [tuple(map(float, line.split())) for line in lines[1:]]

# SVG 생성 (확대 배율 적용)
svg_output = draw_circles_svg(circles, scale=50)

# 파일로 저장
with open("test_circle.svg", "w") as f:
    f.write(svg_output)

print("SVG 파일이 생성되었습니다: circles_large.svg")

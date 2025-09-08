import heapq

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def volume(heightmap):
    if not heightmap or not heightmap[0]:
        return 0

    rows, cols = len(heightmap), len(heightmap[0])
    visited = [[False] * cols for _ in range(rows)]
    min_heap = []

    for r in range(rows):
        for c in range(cols):
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                heapq.heappush(min_heap, (heightmap[r][c], r, c))
                visited[r][c] = True

    water_volume = 0
    while min_heap:
        height, r, c = heapq.heappop(min_heap)

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                water_volume += max(0, height - heightmap[nr][nc])
                heapq.heappush(
                    min_heap, (max(height, heightmap[nr][nc]), nr, nc))
                visited[nr][nc] = True

    return water_volume


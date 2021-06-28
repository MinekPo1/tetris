from typing import Optional
from typing_extensions import TypeGuard
import pygame.constants
import pygame.event
import pygame.surface
import pygame.display
import pygame.image

from glob import glob


def check_if_full(row:list[Optional[int]]) -> TypeGuard[list[int]]:
	return not(None in row)

dead_tiles:list[list[Optional[int]]] = [[None]*10 for i in range(20)]

for i in range(10):dead_tiles[2][i] = 1

w,h = 500,500

win = pygame.display.set_mode((w,h),flags = pygame.constants.RESIZABLE)

blocks = [pygame.image.load(i) for i in glob("./sprites/blocks_[0-9][0-9].png")]
print(len(blocks))

board = pygame.surface.Surface((160,320))

while True:
	for event in pygame.event.get():
		if event.type == pygame.constants.VIDEORESIZE:
			w,h = event.size
		elif event.type == pygame.constants.QUIT:quit()
	if w*2 < h:
		board_rect = (0,(h-(w*2))//2,w,w*2)
	else:
		board_rect = ((w-h//2)//2,0,h//2,h)
	win.fill((0,0,0))
	board.fill((0,0,0))
	for y,row in enumerate(dead_tiles):
		if check_if_full(row):
			for x,tile in enumerate(row):

				t:int = tile
				board.blit(blocks[t],(x*16,y*16))
				if t < 5:
					row[x] = 5
				elif t == 12:
					row[x] = None # type:ignore
					print(":D")
				else:
					row[x] += 1
				continue
		for x,tile in enumerate(row):
			if tile != None:
				board.blit(blocks[tile],(x*16,y*16))

	board_scaled = pygame.transform.scale(board,board_rect[2:])
	win.blit(board_scaled,board_rect[:2])
	pygame.display.flip()

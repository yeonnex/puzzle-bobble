# 버블 이미지 설정 / map 설정

import pygame
import os
pygame.init()
screen_width = 448
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Puzzle Bobble")
clock = pygame.time.Clock()  # 게임 프레임 설정을 위한 객체 생성

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__) # 현재 실행하고 있는 파일의 디렉토리이름을 받아옴
background = pygame.image.load(os.path.join(current_path, 'background.png'))

# 버블 이미지 불러오기
bubble_images = [
    pygame.image.load(os.path.join(current_path, 'red.png')).convert_alpha(),
    pygame.image.load(os.path.join(current_path, 'yellow.png')).convert_alpha(),
    pygame.image.load(os.path.join(current_path, 'blue.png')).convert_alpha(),
    pygame.image.load(os.path.join(current_path, 'green.png')).convert_alpha(),
    pygame.image.load(os.path.join(current_path, 'purple.png')).convert_alpha(),
    pygame.image.load(os.path.join(current_path, 'black.png')).convert_alpha()
]

running = True # 게임 루프를 위한 변수, running. running변수가 True인 동안 계속해서 게임루프가 돌아감
while running:
    clock.tick(60) # FPS 60으로 설정

    for event in pygame.event.get(): # 현재 발생하고 있는 모든 이벤트를 받아옴
        if event.type == pygame.QUIT: # 사용자가 엑스 버튼을 눌렀다면
            running = False

    screen.blit(background, (0,0))
    pygame.display.update() # 업데이트 꼭 해줘야 함. blit() 만 하고 업데이트 하지 않으면 배경화면이 눈에 보이지 않음!

pygame.quit() # 반복문 탈출, pygame 종료. 프로그램 종료

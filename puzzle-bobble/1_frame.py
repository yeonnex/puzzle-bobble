import pygame
pygame.init()
screen_width = 448
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Puzzle Bobble")
clock = pygame.time.Clock()  # 게임 프레임 설정을 위한 객체 생성

running = True # 게임 루프를 위한 변수, running. running변수가 True인 동안 계속해서 게임루프가 돌아감
while running:
    clock.tick(60) # FPS 60으로 설정

    for event in pygame.event.get(): # 현재 발생하고 있는 모든 이벤트를 받아옴
        if event.type == pygame.QUIT: # 사용자가 엑스 버튼을 눌렀다면
            running = False



pygame.quit() # 반복문 탈출, pygame 종료. 프로그램 종료
import pygame, sys, pygame.freetype, random


def if_eat(head_rect, food_rect):
    if food_rect.left <= head_rect.left <= food_rect.right:
        if food_rect.bottom <= head_rect.top <= food_rect.top:
            return True
        elif food_rect.top <= head_rect.bottom <= food_rect.bottom:
            return True
        else:
            return False
    elif food_rect.left <= head_rect.right <= food_rect.right:
        if food_rect.top <= head_rect.top <= food_rect.bottom:
            return True
        elif food_rect.top <= head_rect.bottom <= food_rect.bottom:
            return True
        else:
            return False
    else:
        return False


def create_food(width, height):
    a = random.random() * 600
    b = random.random() * 400
    if a < 100:
        a += 100
    if b < 100:
        b += 100
    if a > width - 100:
        a -= 100
    if b > height - 100:
        b -= 100
    return a, b


def if_over_boundary(head_rect, width, height):
    if head_rect.top <= 0 or head_rect.bottom >= height:
        return True
    elif head_rect.left <= 0 or head_rect.right >= width:
        return True
    else:
        return False


def if_eat_itself(head_rect, snake_body):
    for i in range(1, len(snake_body)):
        if head_rect.left <= snake_body[i].right-2:
            if head_rect.top <= snake_body[i].bottom-2:
                if head_rect.right >= snake_body[i].left+2:
                    if head_rect.bottom >= snake_body[i].top+2:
                        return True
    return False


def direction(speed):
    if speed[0] < 0:
        return 0
    elif speed[0] > 0:
        return 2
    elif speed[1] < 0:
        return 1
    elif speed[1] > 0:
        return 3


def main():
    pygame.init()  # 初始化
    size = width, height = 640, 480
    screen = pygame.display.set_mode(size)  # 设置窗体大小，元组类型
    pygame.display.set_caption("贪吃蛇")  # 设置窗体名字
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    head_rect = pygame.Rect(width / 2, height / 2, 10, 10)
    add_speed = 10
    snake_speed = [0, add_speed]
    snake_body = [head_rect]
    clock = pygame.time.Clock()
    x, y = 100, 100
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_speed[1] == 0:
                    snake_speed[1] -= add_speed
                    snake_speed[0] = 0
                elif event.key == pygame.K_DOWN and snake_speed[1] == 0:
                    snake_speed[0] = 0
                    snake_speed[1] += add_speed
                elif event.key == pygame.K_LEFT and snake_speed[0] == 0:
                    snake_speed[0] -= add_speed
                    snake_speed[1] = 0
                elif event.key == pygame.K_RIGHT and snake_speed[0] == 0:
                    snake_speed[0] += add_speed
                    snake_speed[1] = 0
        screen.fill((255, 255, 255))
        food_rect = pygame.Rect(x, y, 10, 10)
        pygame.draw.rect(screen, RED, food_rect)

        if if_over_boundary(head_rect, width, height) or if_eat_itself(head_rect, snake_body):
            sys.exit()
        if if_eat(head_rect, food_rect):
            x, y = create_food(width, height)
            food_rect = pygame.Rect(x, y, 10, 10)
            pygame.draw.rect(screen, RED, food_rect)
            if direction(snake_speed) == 0:
                temp_rect = pygame.Rect(head_rect.right, head_rect.top, 10, 10)
                snake_body.append(temp_rect)
            if direction(snake_speed) == 1:
                temp_rect = pygame.Rect(head_rect.left, head_rect.bottom, 10, 10)
                snake_body.append(temp_rect)
            if direction(snake_speed) == 2:
                temp_rect = pygame.Rect(head_rect.left-10, head_rect.top, 10, 10)
                snake_body.append(temp_rect)
            if direction(snake_speed) == 3:
                temp_rect = pygame.Rect(head_rect.left, head_rect.top-10, 10, 10)
                snake_body.append(temp_rect)
        for i in range(len(snake_body) - 1):
            snake_body[len(snake_body) - i - 1] = snake_body[len(snake_body) - i - 2]
        head_rect = head_rect.move(snake_speed[0], snake_speed[1])
        snake_body.pop(0)
        snake_body.insert(0, head_rect)
        for i in range(len(snake_body)):
            pygame.draw.rect(screen, GREEN, snake_body[i])
        pygame.display.update()  # 更新
        clock.tick(20)


main()

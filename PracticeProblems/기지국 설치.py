"https://school.programmers.co.kr/learn/courses/30/lessons/12979?language=python3"

"""
N개의 아파트가 일렬로 쭉 늘어서 있습니다. 이 중에서 일부 아파트 옥상에는 4g 기지국이 설치되어 있습니다. 
기술이 발전해 5g 수요가 높아져 4g 기지국을 5g 기지국으로 바꾸려 합니다. 
그런데 5g 기지국은 4g 기지국보다 전달 범위가 좁아, 4g 기지국을 5g 기지국으로 바꾸면 어떤 아파트에는 전파가 도달하지 않습니다.

예를 들어 11개의 아파트가 쭉 늘어서 있고, [4, 11] 번째 아파트 옥상에는 4g 기지국이 설치되어 있습니다. 
만약 이 4g 기지국이 전파 도달 거리가 1인 5g 기지국으로 바뀔 경우 모든 아파트에 전파를 전달할 수 없습니다. 
(전파의 도달 거리가 W일 땐, 기지국이 설치된 아파트를 기준으로 전파를 양쪽으로 W만큼 전달할 수 있습니다.)

이때, 우리는 5g 기지국을 최소로 설치하면서 모든 아파트에 전파를 전달하려고 합니다. 
위의 예시에선 최소 3개의 아파트 옥상에 기지국을 설치해야 모든 아파트에 전파를 전달할 수 있습니다.

아파트의 개수 N, 현재 기지국이 설치된 아파트의 번호가 담긴 1차원 배열 stations, 전파의 도달 거리 W가 매개변수로 주어질 때, 
모든 아파트에 전파를 전달하기 위해 증설해야 할 기지국 개수의 최솟값을 리턴하는 solution 함수를 완성해주세요.
"""

def solution(N, stations, W):
    num_stations = 0
    wave_range = 2 * W + 1  #전파 도달 범위
    last = 0    #마지막으로 커버된 위치

    for station in stations:

        start = max(1, station - W)   #기지국이 커버하는 왼쪽 끝 위치
        end = min(N, station + W)     #기지국이 커버하는 오른쪽 끝 위치

        if last < start - 1:
            to_cover = (start -1) - last   #앞으로 커버해야 할 수

            num_stations += (to_cover + wave_range - 1) // wave_range

        last = end

    if last < N :
        to_cover = N - last
        num_stations += (to_cover + wave_range - 1) // wave_range

    return num_stations


print(solution(11, [4,11], 1))
print(solution(16, [9], 2))




def solution(genres, plays):
    answer = []
    
    # 1. 장르별 총 재생 횟수를 저장할 딕셔너리 (해시)
    # 예: {'classic': 1450, 'pop': 3100}
    genre_total_play = {}
    
    # 2. 장르별 노래 정보(고유 번호, 재생 횟수)를 저장할 딕셔너리
    # 예: {'classic': [(0, 500), (2, 150), (3, 800)], ...}
    genre_songs = {}
    
    # 3. 입력 데이터를 순회하며 딕셔너리에 정보 저장
    # enumerate와 zip을 사용하여 고유 번호(i), 장르(g), 재생 횟수(p)를 한 번에 가져옴
    for i, (g, p) in enumerate(zip(genres, plays)):
        # 해당 장르가 딕셔너리에 없다면 초기화
        if g not in genre_total_play:
            genre_total_play[g] = 0
            genre_songs[g] = []
        
        # 장르별 총 재생 횟수 더하기
        genre_total_play[g] += p
        # 노래 정보 저장 (고유 번호, 재생 횟수) 튜플 형태
        genre_songs[g].append((i, p))
        
    # 4. 장르 선정 기준: 총 재생 횟수가 높은 순으로 정렬
    # 딕셔너리의 items()를 리스트로 변환하여 재생 횟수(x[1]) 기준 내림차순 정렬
    sorted_genres = sorted(genre_total_play.items(), key=lambda x: x[1], reverse=True)
    
    # 5. 각 장르별로 노래 선정 (최대 2곡)
    for g, total in sorted_genres:
        # 해당 장르의 노래 리스트 가져오기
        songs = genre_songs[g]
        
        # 노래 정렬 기준: 
        # 1순위: 재생 횟수(x[1]) 내림차순 (큰 수 -> 작은 수)
        # 2순위: 고유 번호(x[0]) 오름차순 (작은 수 -> 큰 수)
        # 팁: 재생 횟수에 -를 붙여 오름차순 정렬하면, 결과적으로 내림차순 정렬 효과가 남
        songs.sort(key=lambda x: (-x[1], x[0]))
        
        # 6. 정렬된 노래 중 앞에서부터 최대 2개까지만 answer에 추가
        # 장르에 곡이 하나라면 하나만, 두 개 이상이면 두 개 추가
        for i in range(min(len(songs), 2)):
            answer.append(songs[i][0]) # 고유 번호만 추가
            
    return answer
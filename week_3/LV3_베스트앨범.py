def solution(genres, plays):
    answer = []
    best_album = {}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in best_album:
            best_album[genre] = [(i, play)]
        else:
            best_album[genre].append((i, play))

    total_genres = []

    for key in best_album.keys():
        total_genres.append((key, sum([i[1] for i in best_album[key]])))

    total_genres.sort(key=lambda x: -x[1])

    for key, _ in total_genres:
        sorted_plays = sorted(best_album[key], key=lambda x: -x[1])
        cnt = 0
        for i, _ in sorted_plays:
            answer.append(i)
            cnt += 1
            if cnt == 2:
                break
        print(sorted_plays)

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
# result = [4, 1, 3, 0]
print(solution(genres, plays))

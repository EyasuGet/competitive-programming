# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

n , m = map(int, input().split())
durations = []
for _ in range(n):
    rep, time = map(int, input().split())
    dur = list([rep,time])
    durations.append(dur)
    
moments = list(map(int, input().split()))
prefix = []
cum_minute = 0
for durr in durations:
    rep, time = durr
    cum_minute += rep * time
    prefix.append(cum_minute)

song_idx = 0
for i in moments:
    # print(song_idx, i , prefix[song_idx])
    while song_idx < n and prefix[song_idx] < i:
        song_idx += 1
    print(song_idx+1)


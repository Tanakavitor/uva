def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    n = int(data[0].strip())
    index = 1

    for i in range(n):
        torneio = data[index].strip()
        index += 1
        n_times = int(data[index].strip())
        index += 1

        times = []
        for _ in range(n_times):
            times.append(data[index].strip())
            index += 1

        ranking = {team: {"pontos": 0, "games_played": 0, "goal_difference": 0, "goals_scored": 0, "goals_against": 0, "wins": 0, "ties": 0, "losses": 0} for team in times}

        n_jogos = int(data[index].strip())
        index += 1

        for _ in range(n_jogos):
            parts = data[index].split('#')
            index += 1
            team_name_1 = parts[0]
            goals1, goals2 = map(int, parts[1].split('@'))
            team_name_2 = parts[2]

            if goals1 == goals2:
                ranking[team_name_1]["pontos"] += 1
                ranking[team_name_2]["pontos"] += 1
                ranking[team_name_1]["ties"] += 1
                ranking[team_name_2]["ties"] += 1
            elif goals1 > goals2:
                ranking[team_name_1]["pontos"] += 3
                ranking[team_name_1]["wins"] += 1
                ranking[team_name_2]["losses"] += 1
            else:
                ranking[team_name_2]["pontos"] += 3
                ranking[team_name_2]["wins"] += 1
                ranking[team_name_1]["losses"] += 1

            ranking[team_name_1]["games_played"] += 1
            ranking[team_name_2]["games_played"] += 1
            ranking[team_name_1]["goal_difference"] += (goals1 - goals2)
            ranking[team_name_2]["goal_difference"] += (goals2 - goals1)
            ranking[team_name_1]["goals_scored"] += goals1
            ranking[team_name_1]["goals_against"] += goals2
            ranking[team_name_2]["goals_scored"] += goals2
            ranking[team_name_2]["goals_against"] += goals1

        sorted_ranking = sorted(ranking.items(), key=lambda x: (-x[1]['pontos'], -x[1]['wins'], -x[1]['goal_difference'], -x[1]['goals_scored'], x[1]['games_played'], x[0].lower()))

        print(torneio)
        for j, (team, stats) in enumerate(sorted_ranking, start=1):
            print(f"{j}) {team} {stats['pontos']}p, {stats['games_played']}g ({stats['wins']}-{stats['ties']}-{stats['losses']}), {stats['goal_difference']}gd ({stats['goals_scored']}-{stats['goals_against']})")
        if i < n - 1:
            print()

if __name__ == "__main__":
    main()
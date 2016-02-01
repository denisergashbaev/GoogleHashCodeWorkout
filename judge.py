import read_input_file
from balloon import Balloon


def evaluate_output(config, output_file):
    T = config['T']
    balloons = [Balloon(index, config) for index in range(config['B'])]
    final_score = 0
    with open(output_file, 'r') as f:
        lines = f.readlines()
        for turn in range(T):
            turn_score = 0
            line = lines[turn]
            for idx, level in enumerate(read_input_file.get_line(line)):
                balloons[idx].level = level
            for balloon in balloons:
                if not balloon.lost and balloon.level > 0:
                    wind = config['a_map'][balloon.level - 1][balloon.current_cell[0]][balloon.current_cell[1]]
                    balloon.apply_wind(wind)
                    turn_score += balloon.calc_targets_covered()
            print "%s points at the end of turn %s" % (turn_score, turn)
            final_score += turn_score
    print "Your final score is: %s" % final_score


if __name__ == "__main__":
    config = read_input_file.load_configuration('test_input')
    evaluate_output(config, "test_output")
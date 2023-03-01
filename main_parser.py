from parsers.MindBugsParser import MindBugsParser


def parse_mindbugs():
    nbp = MindBugsParser("datasets/mb_ds/fakenews.csv")
    nbp.parse_dataset()
    nbp.set_owner("MindBugs@techwave.ro")
    final_df = nbp.get_final_df()
    print(final_df.head())
    final_df.to_csv("datasets/mb_ds/parsed_dataset.csv")


if __name__ == '__main__':
    parse_mindbugs()
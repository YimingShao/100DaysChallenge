import research
import cProfile

profiler = cProfile.Profile()
profiler.disable()


def main():
    print("Weather research for Seattle, 2014-2015")
    print()
    profiler.enable()



    research.init()

    print("The hottest 5 days:")
    hot_days = research.hot_days()
    cold_days = research.cold_days()
    wet_days = research.wet_days()

    for idx, d in enumerate(hot_days[:5]):
        print("{}. {} F on {}".format(idx+1, d.actual_max_temp, d.date))
    print()
    print("The coldest 5 days:")

    for idx, d in enumerate(cold_days[:5]):
        print("{}. {} F on {}".format(idx+1, d.actual_min_temp, d.date))
    print()
    print("The wettest 5 days:")


    for idx, d in enumerate(wet_days[:5]):
        print("{}. {} inches of rain on {}".format(idx+1, d.actual_precipitation, d.date))

    profiler.disable()

if __name__ == '__main__':
    main()

    profiler.print_stats(sort='cumtime')
import api
import cProfile


profiler = cProfile.Profile()
profiler.disable()

def main():
    profiler.enable()
    api.scrape()
    profiler.disable()


if __name__ == '__main__':
    main()
    profiler.print_stats(sort='cumtime')
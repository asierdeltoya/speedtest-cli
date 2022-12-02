import speedtest

s = speedtest.Speedtest()
s.get_servers()
s.get_best_server()
s.download()
s.upload()
results_dict = s.results.dict()

print(results_dict)
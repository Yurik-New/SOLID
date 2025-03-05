class ReportGenerator:
    def generate(self, data):
        return f"Report: {data}"

class ReportSaver:
    def save(self, report, filename) :
        with open (filename, 'w') as file:
            file.write(report)

# Використання
report = ReportGenerator().generate("Sales Data")
ReportSaver().save(report, "report.txt")
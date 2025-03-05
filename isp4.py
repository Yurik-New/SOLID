from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class AllInOnePrinter(Printer, Scanner):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self):
        return "Scanned document"

# Використання
printer = AllInOnePrinter()
printer.print_document("Test file")
print(printer.scan_document())

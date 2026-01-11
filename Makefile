# Makefile for Hospital Records Data Pipeline
# Run: make all

.PHONY: all clean validate process analyze help

# Default target
all: validate process analyze

# Help message
help:
	@echo "Hospital Records Data Pipeline"
	@echo "=============================="
	@echo ""
	@echo "Available targets:"
	@echo "  make all       - Run complete pipeline (validate + process + analyze)"
	@echo "  make validate  - Validate raw data"
	@echo "  make process   - Clean and process data"
	@echo "  make analyze   - Generate analysis reports"
	@echo "  make clean     - Remove processed data and reports"
	@echo "  make help      - Show this help message"
	@echo ""

# Validate raw data
validate:
	@echo "Step 1: Validating raw data..."
	python src/validate_data.py

# Process and clean data
process: validate
	@echo "Step 2: Cleaning data..."
	python src/clean_data.py

# Generate analysis
analyze: process
	@echo "Step 3: Analyzing data..."
	python src/analyze_data.py
	@echo ""
	@echo "✓ Pipeline complete! Check reports/ folder for outputs."

# Clean generated files
clean:
	@echo "Cleaning processed data and reports..."
	rm -rf data/processed/*
	rm -rf data/interim/*
	rm -rf reports/*
	@echo "✓ Clean complete"
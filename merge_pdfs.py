#!/usr/bin/env python3
"""
PDF Merger Script for Software Solution Engineer Roadmap
Merges three roadmap PDFs in sequential order:
1. Full Stack Development
2. AI Engineer
3. Software Architect
"""

from PyPDF2 import PdfMerger
import sys

def merge_pdfs():
    """Merge three PDF roadmaps into a comprehensive Software Solution Engineer roadmap."""
    
    # Define input files in the desired order
    input_files = [
        'full-stack.pdf',
        'ai-engineer.pdf',
        'software-architect.pdf'
    ]
    
    # Output file name
    output_file = 'software-solution-engineer-roadmap.pdf'
    
    print("=" * 70)
    print("Software Solution Engineer Roadmap - PDF Merger")
    print("=" * 70)
    print()
    
    try:
        # Create PDF merger object
        merger = PdfMerger()
        
        # Add each PDF in order
        for i, pdf_file in enumerate(input_files, 1):
            print(f"[{i}/{len(input_files)}] Adding: {pdf_file}")
            merger.append(pdf_file)
            print(f"    ✓ Successfully added {pdf_file}")
        
        print()
        print(f"Merging PDFs into: {output_file}")
        
        # Write the merged PDF
        merger.write(output_file)
        merger.close()
        
        print(f"    ✓ Successfully created {output_file}")
        print()
        print("=" * 70)
        print("Merge Complete!")
        print("=" * 70)
        print()
        print("Your comprehensive Software Solution Engineer roadmap is ready:")
        print(f"  → {output_file}")
        print()
        print("Learning Path Order:")
        print("  1. Full Stack Development (Foundation)")
        print("  2. AI Engineering (Specialization)")
        print("  3. Software Architecture (Advanced)")
        print()
        
        return True
        
    except FileNotFoundError as e:
        print(f"✗ Error: Could not find file - {e}")
        return False
    except Exception as e:
        print(f"✗ Error during merge: {e}")
        return False

if __name__ == "__main__":
    success = merge_pdfs()
    sys.exit(0 if success else 1)

# Made with Bob

#!/usr/bin/env python3
"""Offline manuscript regressions; not a substitute for a fresh-reader review."""
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def sources():
    names = re.findall(r'^\s*-\s+([^\s]+\.qmd)\s*$',
                       (ROOT / '_quarto.yml').read_text(), re.M)
    return {name: (ROOT / name).read_text() for name in names}


class ManuscriptChecks(unittest.TestCase):
    def test_reading_order(self):
        files = sources()
        self.assertEqual(len(files), 20)
        chapters = [Path(p).stem for p in files if p.startswith('chapters/')]
        self.assertEqual(chapters, [
            'the-delegation-trap', 'what-is-ai', 'what-are-llms',
            'does-ai-make-us-dumber', 'ai-last', 'the-conversation-loop',
            'staying-critical', 'vet-your-ai', 'is-prompting-dead',
            'prompt-chaining', 'seven-techniques', 'using-ai-to-help-you-use-ai',
            'conversations-across-disciplines', 'when-the-loop-runs-itself',
            'becoming-more-capable'])

    def test_cross_references(self):
        files = sources()
        ids = set(re.findall(r'\{#([\w-]+)', '\n'.join(files.values())))
        for name, text in files.items():
            text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
            for ref in re.findall(r'@(sec-[\w-]+)', text):
                with self.subTest(file=name, reference=ref):
                    self.assertIn(ref, ids)
            for href in re.findall(r'\]\(([^)]+)\)', text):
                link = urlsplit(href)
                if link.scheme or not link.path or link.path.startswith('/'):
                    continue
                with self.subTest(file=name, link=href):
                    self.assertTrue((ROOT / name).parent.joinpath(unquote(link.path)).exists())

    def test_workshop_arithmetic_and_boundary(self):
        case = sources()['chapters/conversations-across-disciplines.qmd']
        capacity = int(re.search(r'maximum (\d+) people', case).group(1))
        participants = int(re.search(r'P1: attendance \| (\d+) participants', case).group(1))
        budget = int(re.search(r'Maximum AUD (\d+)', case).group(1))
        self.assertEqual((capacity, participants, budget), (12, 18, 80))
        self.assertGreater(12 + 2, capacity)
        self.assertGreater(45 * 2 + 10, 90)
        self.assertLessEqual(participants // 2 + 2, capacity)
        self.assertEqual(35 * 2 + 10 + 10, 90)
        self.assertEqual(participants * 2 + 30 + 10, 76)
        self.assertIn('14:00–14:35', case)
        self.assertIn('14:35–14:45', case)
        self.assertIn('14:45–15:20', case)
        self.assertIn('15:20–15:30', case)
        self.assertEqual(20 // 2 + 2, capacity)
        self.assertEqual(40 * 2 + 10 + 10, 100)
        self.assertEqual(20 * 2 + 30 + 10, budget)
        for text in ['constructed teaching examples', '18 × 2 + 30 + 10 = 76',
                     '20 × 2 + 30 + 10 = 80', 'confirmation as outstanding']:
            self.assertIn(text, case)

    def test_practice_is_varied_and_accessible(self):
        files = sources()
        chapters = [text for name, text in files.items() if name.startswith('chapters/')]
        self.assertLessEqual(sum('## Take it to the AI' in text for text in chapters), 3)
        self.assertGreaterEqual(sum('**Time:**' in text for text in chapters), 10)
        case = files['chapters/conversations-across-disciplines.qmd']
        self.assertIn('No AI required', case)
        self.assertIn('dictation', case)
        self.assertIn('Verify, Explain, Test', case)


if __name__ == '__main__':
    unittest.main(verbosity=2)

from typing import Optional, Sequence, List, Tuple

def get_alignments(a: Sequence[str], b: Sequence[str]) -> Tuple[List[List[int]]]: ...
def get_charmap(a: str, b: str) -> Tuple[List[Optional[int]], List[Optional[int]]]: ...

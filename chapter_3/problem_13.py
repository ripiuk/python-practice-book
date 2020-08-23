"""
Problem:
    Write a program `csv2xls.py` that reads a csv file and exports it as Excel file.
    The program should take two arguments. The name of the csv file to read as
    first argument and the name of the Excel file to write as the second argument.
"""


import sys
import csv
from pathlib import Path

from openpyxl import Workbook


def main(csv_file_path: str, xls_file_path: str) -> None:
    """Convert CSV file to Excel file

    Not existing csv file:
        >>> main(csv_file_path='not_existing_file.csv', xls_file_path='res.xlsx')
        Can not find CSV file: 'not_existing_file.csv'

    Reading csv file error:
        >>> import tempfile
        >>> from unittest import mock
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     csv_f = Path(tmp_dir) / f'test_file.csv'
        ...     csv_f.touch()
        ...     xls_f = Path(tmp_dir) / f'res_file.xlsx'
        ...     with mock.patch('chapter_3.problem_13.csv') as csv_mock:
        ...         csv_mock.reader.side_effect = UnicodeDecodeError('err msg', b'', 1, 1, 'here')
        ...         main(csv_file_path=str(csv_f), xls_file_path=str(xls_f))
        Can not convert file '/tmp/.../test_file.csv'.
        Error: 'err msg' codec can't decode bytes in position 1-0: here

    Successfully converted CSV file:
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     csv_f = Path(tmp_dir) / f'test_file.csv'
        ...     _ = csv_f.write_text('1, 2, 3')
        ...     xls_f = Path(tmp_dir) / f'res_file.xlsx'
        ...     main(csv_file_path=str(csv_f), xls_file_path=str(xls_f))
        ...     assert xls_f.exists()
        ...     assert xls_f.stat().st_size >= 4800
        Successfully converted CSV file '/tmp/.../test_file.csv' -> to Excel file '/tmp/.../res_file.xlsx'

    Add suffix to Excel file if not exists:
        >>> with tempfile.TemporaryDirectory() as tmp_dir:
        ...     csv_f = Path(tmp_dir) / f'test_file.csv'
        ...     _ = csv_f.write_text('test text')
        ...     res_f = Path(tmp_dir) / f'res_file'
        ...     main(csv_file_path=str(csv_f), xls_file_path=str(res_f))
        ...     assert not res_f.exists()
        ...     xls_f = Path(tmp_dir) / f'res_file.xlsx'
        ...     assert xls_f.exists()
        ...     assert xls_f.stat().st_size >= 4700
        Successfully converted CSV file '/tmp/.../test_file.csv' -> to Excel file '/tmp/.../res_file.xlsx'

    :param csv_file_path: local path to a CSV file.
    :param xls_file_path: local path to a Excel file.
    :return: None.
    """
    csv_file_path = Path(csv_file_path)
    if not csv_file_path.exists():
        print(f'Can not find CSV file: {str(csv_file_path)!r}')
        return

    if Path(xls_file_path).suffix != '.xlsx':
        xls_file_path = f'{xls_file_path}.xlsx'

    wb = Workbook()
    try:
        with open(str(csv_file_path), 'r', encoding='utf-8') as csv_f:
            for row in csv.reader(csv_f):
                wb.active.append(row)
        wb.save(xls_file_path)
    except UnicodeDecodeError as err:
        print(f'Can not convert file {str(csv_file_path)!r}.\nError: {err}')
        return
    finally:
        wb.close()
    print(
        f'Successfully converted CSV file {str(csv_file_path)!r} -> '
        f'to Excel file {xls_file_path!r}'
    )


if __name__ == "__main__":
    main(
        csv_file_path=sys.argv[1],
        xls_file_path=sys.argv[2],
    )

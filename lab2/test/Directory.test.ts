import { Directory } from './../src/Directory';

describe('Directory', () => {
  const OLD_ENV = process.env;

  beforeAll(() => {
    process.env = {
      ...OLD_ENV,
      DIR_MAX_ELEMS: '2',
    };
  });

  afterAll(() => {
    process.env = OLD_ENV;
  });

  const rootDir = new Directory(null, 'root');

  test('should be successfully created', () => {
    expect(() => new Directory(rootDir)).not.toThrowError();
  });

  const dirname = 'dirname';
  const dir = new Directory(rootDir, dirname);

  test('contains proper items', () => {
    expect(rootDir.content[0].name).toEqual(dir.name);
  });

  test('should have a proper dirname', () => {
    expect(dir.name).toBe(dirname);
  });

  test('should have a proper parent', () => {
    expect(dir.parent).toBe(rootDir);
  });

  test('should have a proper default files', () => {
    expect(dir.content.length).toBe(0);
  });

  test('moving the root directory', () => {
    expect(() => {
      const newDir = new Directory(null, 'newDir');
      rootDir.moveTo(newDir);
    }).toThrowError();
  });

  test('overflowing the directory', () => {
    expect(() => {
      dir.addFile(new Directory(null, 'dir1'));
      dir.addFile(new Directory(null, 'dir2'));
      dir.addFile(new Directory(null, 'dir3'));
    }).toThrowError();
  });
});

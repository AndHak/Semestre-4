import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BotonesComponent } from './botones.component';

describe('BotonesComponent', () => {
  let component: BotonesComponent;
  let fixture: ComponentFixture<BotonesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BotonesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BotonesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
